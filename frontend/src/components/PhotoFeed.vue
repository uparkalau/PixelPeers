<template>
    <div class="photo-feed">
      <div v-for="photo in photos" :key="photo.id" class="photo-item">
        <img :src="photo.url" :alt="photo.caption">
        <p>{{ photo.caption }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'
  
  export default {
    name: 'PhotoFeed',
    computed: {
      ...mapState(['photos'])
    },
    methods: {
      ...mapActions(['fetchPhotos'])
    },
    created() {
      this.fetchPhotos()
    }
  }
  </script>