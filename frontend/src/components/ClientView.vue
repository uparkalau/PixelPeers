<template>
    <div class="client-view">
      <h2>Your Gallery</h2>
      <p>Your public gallery: {{ publicUrl }}</p>
      <photo-gallery :photos="userPhotos"></photo-gallery>
      <template-editor v-if="hasCustomTemplate"></template-editor>
    </div>
  </template>
  
  <script>
  import { mapState, mapGetters, mapActions } from 'vuex'
  import PhotoGallery from './PhotoGallery.vue'
  import TemplateEditor from './TemplateEditor.vue'
  
  export default {
    name: 'ClientView',
    components: {
      PhotoGallery,
      TemplateEditor
    },
    computed: {
      ...mapState(['userPhotos', 'currentUser']),
      ...mapGetters(['hasCustomTemplate']),
      publicUrl() {
        return `http://${this.currentUser.subdomain}.yourapp.com`
      }
    },
    methods: {
      ...mapActions(['fetchUserPhotos'])
    },
    created() {
      this.fetchUserPhotos(this.currentUser.id)
    }
  }
  </script>