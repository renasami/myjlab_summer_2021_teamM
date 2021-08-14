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
</script>

<style scoped>
.profile {
  width:82%;
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
    margin-top: 30px;
}

.btn:hover {
    color: #418cb571 !important;
}
</style>
