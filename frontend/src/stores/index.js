import { createStore } from 'vuex'
import axios from 'axios'

const API_URL = 'http://localhost:5000'

export default createStore({
  state: {
    photos: [],
    userPhotos: [],
    templates: [],
    subdomains: [],
    users: [],
    currentUser: null
  },
  mutations: {
    setPhotos(state, photos) { state.photos = photos },
    setUserPhotos(state, photos) { state.userPhotos = photos },
    setTemplates(state, templates) { state.templates = templates },
    setSubdomains(state, subdomains) { state.subdomains = subdomains },
    setUsers(state, users) { state.users = users },
    setCurrentUser(state, user) { state.currentUser = user }
  },
  actions: {
    async fetchPhotos({ commit }) {
      const response = await axios.get(`${API_URL}/photos`)
      commit('setPhotos', response.data)
    },
    async fetchUserPhotos({ commit }, userId) {
      const response = await axios.get(`${API_URL}/photos/user/${userId}`)
      commit('setUserPhotos', response.data)
    },
    async fetchTemplates({ commit }) {
      const response = await axios.get(`${API_URL}/templates`)
      commit('setTemplates', response.data)
    },
    async updateTemplate({ commit }, template) {
      await axios.put(`${API_URL}/templates/${template.id}`, template)
      // Refresh templates after update
      const response = await axios.get(`${API_URL}/templates`)
      commit('setTemplates', response.data)
    },
    async fetchSubdomains({ commit }) {
      const response = await axios.get(`${API_URL}/subdomains`)
      commit('setSubdomains', response.data)
    },
    async createSubdomain({ commit }, subdomain) {
      await axios.post(`${API_URL}/subdomains`, subdomain)
      // Refresh subdomains after creation
      const response = await axios.get(`${API_URL}/subdomains`)
      commit('setSubdomains', response.data)
    },
    async deleteSubdomain({ commit }, subdomainId) {
      await axios.delete(`${API_URL}/subdomains/${subdomainId}`)
      // Refresh subdomains after deletion
      const response = await axios.get(`${API_URL}/subdomains`)
      commit('setSubdomains', response.data)
    },
    async fetchUsers({ commit }) {
      const response = await axios.get(`${API_URL}/users`)
      commit('setUsers', response.data)
    },
    async login({ commit }, credentials) {
      const response = await axios.post(`${API_URL}/login`, credentials)
      commit('setCurrentUser', response.data)
    }
  },
  getters: {
    hasCustomTemplate: (state) => {
      return state.currentUser && state.currentUser.hasCustomTemplate
    }
  }
})