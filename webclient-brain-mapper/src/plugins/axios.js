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
    if(error.response) {
      // At any moment if response status is 401 emits an event that logout user
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        emitter.emit('session-exp');
      }
      else emitter.emit('response-error');
    }
    else { // Something happened with response that triggered an Error
      emitter.emit("server-error");
    }

    return Promise.reject(error);
  },
);

export default axiosInstance;