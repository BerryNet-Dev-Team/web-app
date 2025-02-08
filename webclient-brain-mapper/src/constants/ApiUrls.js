export default {
  // Auth URLS
  register: '/auth/register',
  login: '/auth/login',
  isLoggedIn: '/auth/isLoggedIn',
  getUserRole: '/auth/getUserRole',
  logout: '/auth/logout',

  // Scenes URLS
  getScenePresignedUrl: '/scenes/getScenePresignedUrls',
  addScene: '/scenes/addScene',

  // Inferences URLS
  getBaseImgPresignedUrls: '/inferences/getBaseImgPresignedUrls',
  generateInference: '/inferences/generateInference',
};
