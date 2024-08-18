<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/">Home</router-link> |
        <!-- <router-link to="/profile">Profile</router-link> -->
      </nav>
    </header>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>