<template>
    <div class="template-editor">
      <h3>Template Editor</h3>
      <select v-model="selectedTemplate">
        <option v-for="template in templates" :key="template.id" :value="template.id">
          {{ template.name }}
        </option>
      </select>
      <textarea v-model="templateContent" rows="10"></textarea>
      <button @click="saveTemplate">Save Template</button>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'
  
  export default {
    name: 'TemplateEditor',
    data() {
      return {
        selectedTemplate: null,
        templateContent: ''
      }
    },
    computed: {
      ...mapState(['templates'])
    },
    methods: {
      ...mapActions(['fetchTemplates', 'updateTemplate']),
      saveTemplate() {
        this.updateTemplate({
          id: this.selectedTemplate,
          content: this.templateContent
        })
      }
    },
    created() {
      this.fetchTemplates()
    },
    watch: {
      selectedTemplate(newVal) {
        const template = this.templates.find(t => t.id === newVal)
        if (template) {
          this.templateContent = template.content
        }
      }
    }
  }
  </script>