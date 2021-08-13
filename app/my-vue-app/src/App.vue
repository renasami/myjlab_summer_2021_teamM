<template height="100%">
  <div id="app">
    <router-view/>
    <Navber/>
  </div>
</template>
<script>
import Navber from './components/Navber'
export default {
  name: 'App',
  components: {
  Navber
  }
}
</script>

<style>
</style>
