import axios from 'axios'
import emitter from './emitter';

const axiosInstance = axios.create({
  withCredentials: true,
  baseURL: import.meta.env.VITE_API_BASE_URL
});

axiosInstance.interceptors.request.use(
  (conf) => {
    emitter.emit('before-request');
    return conf;
  },
  (error) => {
    emitter.emit('request-error');
    return Promise.reject(error);
  },
);

axiosInstance.interceptors.response.use(
  (response) => {
    emitter.emit('after-response');
    return response;
  },
  (error) => {
    try {
      const originalRequest = error.config;

      // At any moment if response status is 401 emits an event that logout user
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        emitter.emit('session-exp');
      }
      else emitter.emit('response-error');

      return Promise.reject(error);
    }
    catch (err) {
      return Promise.reject(new Error('server_error'));
    }
  },
);

export default axiosInstance;