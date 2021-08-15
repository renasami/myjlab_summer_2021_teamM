<template>
<div id='nav'>
<div class='nav_inner'>
<div class='nav_inner2'>


<img id='logo' alt="VG logo" src="./img/vglogo.svg"><br>
<img id='profile_pic' alt="Profile pic" src="./img/Profile.png">
<h3>Yutaka Miyaji</h3>

<ul>

            <li><a><router-link to="/home"><span class='router_box'><svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" viewBox="0 -10 28 33" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20 9v11a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V9"/><path d="M9 22V12h6v10M2 10.6L12 2l10 8.6"/></svg><span class='router_text'>Home</span></span></router-link></a></li>
            <li><a><router-link to="/like"><span class='router_box'><svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" viewBox="0 -10 28 33" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg><span class='router_text'>Repeat Likes</span></span></router-link></a></li>
            <li><a><router-link to="/profile"><span class='router_box'><svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" viewBox="0 -10 28 33" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg><span class='router_text'>User Profile</span></span></router-link></a></li>
            <li><a @click="logout"><span class='router_box'><svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" viewBox="0 -10 28 33" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M16 17l5-5-5-5M19.8 12H9M10 3H4v18h6"/></svg><span class='router_text'>Logout</span></span></a></li>
</ul>


<a @click="createModal" class="btn"><span>+ Post Video</span></a>



</div>
</div>
</div>
</template>



<script>

export default {
  methods: {
    createModal(){
      console.log("createModal")
      
      this.$emit('createModal')
    },
    logout(){
        console.log("logout")
        
        document.cookie = "isLogin=; expires=0";
        document.cookie = "isLogin=false"
        location.href="/login"
    }
  }
}

</script>


<style scoped>
#nav {
text-align: center;
}

/* #nav li a {
    height: 30px;
    display:block;
} */

#nav a.router-link-exact-active {
    color: #CF2E92;
}

#nav a .router-link-exact-active .router_box{
    background: linear-gradient(to right, #CF2E92 5px, rgba(0, 0, 0, 0) 5px);
}

#nav .router_text {
    margin-left: 10px;
}

svg {
    margin-left: 35px;
    margin-top: 10px;
}

#nav a .router-link-exact-active svg{
    stroke: #CF2E92;
}

.nav_inner {
    height: 93%;
    width: 95%;
    position: absolute;
    text-align: center;
    top: 50%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
    color: #231815;
}

.nav_inner2 {
    height:100%;
    position:relative;
}

#profile_pic {
    width: 120px;
    border-radius:100vh;
    margin-top:20px;
}

h3 {
    margin-top:0px;
}


ul {
    width:100%;
    list-style:none;
    margin-top: 20px;
}

li {
    margin-top: 5px;
    text-align:left;
}


a {
    text-decoration: none;
}

#logo {
    width:140px;
}


.btn { 
    width:150px;
    display: inline-block;
    color: white !important;
    font-weight: bold;
    padding-top: 12px;
    padding-bottom: 12px;
    border-radius:100vh;
    outline: none;
    /*背景の色と形状*/
    background: linear-gradient(270deg, #FFDD83 10%, #CF2E92 90%);
    background-position: 1% 50%;
    background-size: 130% auto;
    /*アニメーションの指定*/
    transition: all 0.3s ease-out;
    position: absolute;
    top: 93%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
}

.btn:hover {
    color: #fff;
    background-position: 99% 50%;
}
</style>