<template>
<h1>Like Page</h1>
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

export default {
    
}
</script>r