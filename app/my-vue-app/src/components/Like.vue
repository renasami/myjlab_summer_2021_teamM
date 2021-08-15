<template>
    <div>
        <Card/>
    </div>
</template>
<script>

window.onload = function(){
    let cookies = document.cookie; //全てのcookieを取り出して
let cookiesArray = cookies.split(';'); // ;で分割し配列に
    console.log(location.href)
    if (document.cookie == "" & location.pathname == "/like") location.href = "/login";
    for(var c of cookiesArray){ //一つ一つ取り出して
        var cArray = c.split('='); //さらに=で分割して配列に
        if( cArray[0] == ' isLogin'){
            if(cArray[1] == " false" & location.pathname == "/like"){
                location.href = "/login";
                return
            }  // [key,value] 
        }
    }
}
import Card from './Card.vue'
export default {
    name:"like"  ,
    components:{
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