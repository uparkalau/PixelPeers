<template>
    <div class="admin-panel">
      <h2>Admin Panel</h2>
      <template-editor></template-editor>
      <subdomain-manager></subdomain-manager>
    </div>
  </template>
  
  <script>
  import TemplateEditor from './TemplateEditor.vue'
  import SubdomainManager from './SubdomainManager.vue'
  
  export default {
    name: 'AdminPanel',
    components: {
      TemplateEditor,
      SubdomainManager
    }
  }
  </script>