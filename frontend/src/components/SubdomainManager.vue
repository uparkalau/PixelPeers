<template>
    <div class="subdomain-manager">
      <h3>Subdomain Manager</h3>
      <ul>
        <li v-for="subdomain in subdomains" :key="subdomain.id">
          {{ subdomain.name }} - {{ subdomain.user }}
          <button @click="deleteSubdomain(subdomain.id)">Delete</button>
        </li>
      </ul>
      <div>
        <input v-model="newSubdomain" placeholder="New subdomain">
        <select v-model="selectedUser">
          <option v-for="user in users" :key="user.id" :value="user.id">{{ user.username }}</option>
        </select>
        <button @click="createSubdomain">Create Subdomain</button>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'
  
  export default {
    name: 'SubdomainManager',
    data() {
      return {
        newSubdomain: '',
        selectedUser: null
      }
    },
    computed: {
      ...mapState(['subdomains', 'users'])
    },
    methods: {
      ...mapActions(['fetchSubdomains', 'createSubdomain', 'deleteSubdomain', 'fetchUsers']),
      async createSubdomain() {
        await this.createSubdomain({
          name: this.newSubdomain,
          userId: this.selectedUser
        })
        this.newSubdomain = ''
        this.selectedUser = null
      }
    },
    created() {
      this.fetchSubdomains()
      this.fetchUsers()
    }
  }
  </script>