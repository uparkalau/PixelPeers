<template>
    <div class="home">
      <h1>Welcome to PhotoNet</h1>
      <photo-feed></photo-feed>
    </div>
  </template>
  
  <script>
  import PhotoFeed from '@/components/PhotoFeed.vue'
  
  export default {
    name: 'Home',
    components: {
      PhotoFeed
    }
  }
  </script>