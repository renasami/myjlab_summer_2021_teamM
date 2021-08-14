<template>
<div class='profile'>
     <div class="profile_inner">
         <img class='profile_img' src="./img/Profile.png"><br>
         <input type="text" id="name" name="name" placeholder="User Name"><br>
         <input type="text" id="password" name="name" placeholder="Password"><br>
         <a href="" class="btn"><span>完了</span></a>
     </div>
</div>
</template>

<script>
let cookies = document.cookie; //全てのcookieを取り出して
let cookiesArray = cookies.split(';'); // ;で分割し配列に
if (document.cookie == "" & location.pathname == "/like") location.href = "/login";
for(var c of cookiesArray){ //一つ一つ取り出して
    var cArray = c.split('='); //さらに=で分割して配列に
    if( cArray[0] == ' isLogin' & location.pathname == "/profile"){ // 取り出したいkeyと合致したら
        if(cArray[1] == "false") location.href = "/login"  // [key,value] 
    }
}
</script>

<style scoped>
.profile {
  width:80%;
  position: absolute;
  right: 0;
  height: 100vh;
}

.profile_inner {
    position: absolute;
    width:60%;
    top: 50%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
}

.profile_img {
    width: 40%;
    border-radius: 3px;
}

#name {
    margin-top: 20px;
}

#password {
    margin-top: 10px;
}

input {
    width:130px;
    height:20px;
}


.btn { 
    display: inline-block;
    color: #418DB5 !important;
    outline: none;
    font-weight: bold;
    text-decoration: none;
    margin-top: 20px;
}

.btn:hover {
    color: #418cb571 !important;
}
</style>
