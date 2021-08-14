<template>
<div class='profile'>
     <div class="profile_inner">
         <img class='profile_img' src="./img/Profile.png"><br>
         <input type="text" id="name" name="name"><br>
         <input type="text" id="password" name="name"><br>
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
}

.profile_inner {
    width:60%;
    margin: 0 auto;
    background-color: #F7F7F7;
}

.profile_img {
    width: 40%;
}

.btn { 
    display: inline-block;
    color: #418DB5 !important;
    outline: none;
    font-weight: bold;
    text-decoration: none;
}

.btn:hover {
    color: #418cb571 !important;
}
</style>
