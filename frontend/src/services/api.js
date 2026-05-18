import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
});

export const getUsers = () => api.get('/users');
export const getUserById = (id) => api.get(`/users/${id}`);
export const getRandomUser = () => api.get('/users/random');
export const loadUsers = (count) => api.post(`/users/load?count=${count}`);

export default api;