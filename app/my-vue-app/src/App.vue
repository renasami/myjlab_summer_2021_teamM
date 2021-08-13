<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Navber/>
  </div>
</template>

<script>
import Navber from './components/Navber.vue'

export default {
  name: 'App',
  components: {

    Navber
  }
}
</script>

<style>
* {
  color: #231815;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  height: 100vh;
}
#nav {
  position: fixed;
  background-color: #F7F7F7;
  top:0;
  width:250px;
  height:100vh;
}
</style>
