<template>
    <div>
        <Card/>
    </div>
</template>

<script>
import Card from './Card'
// let cookies = document.cookie; //全てのcookieを取り出して
// let cookiesArray = cookies.split(';'); // ;で分割し配列に
// if (document.cookie == "" & location.pathname == "/home") location.href = "/login";
// for(var c of cookiesArray){
//     let cArray = c.split('=')
//     if(cArray[0] == ' isLogin' & location.pathname == "/home"){ 
//         if(cArray[1] == "false") location.href = "/login" 
//     }
// }

export default {
    name: 'Home',
    components: {
        Card
    },
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