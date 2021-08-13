<template height="100%">
  <div id="app">
    <router-view/>
  </div>
</template>


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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;

}
</style>
