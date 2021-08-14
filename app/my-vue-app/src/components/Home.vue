<template>
    <div>
        <Card/>
    </div>
</template>

<script>
import Card from './Card'

export default {
    name: 'Home',
    components: {
        Card
    }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #231815;
  margin-top: 0px;
  height: 100vh;
}

#nav {
  position: fixed;
  background-color: #F7F7F7;
  top:0;
  width:20%;
  height:100vh;
}

#nav a {
  color: #231815;
}
</style>