<template>
<div id='nav'>
<div class='nav_inner'>
<div class='nav_inner2'>


<img id='logo' alt="VG logo" src="./img/vglogo.png">
<img id='profile_pic' alt="Profile pic" src="./img/profile.jpg">
<h3>User Name</h3>

<ul>
            <li><a><router-link to="/home">Home</router-link></a></li>
            <li><a><router-link to="/like">Like</router-link></a></li>
            <li><a><router-link to="/user">User Profile</router-link></a></li>
            <li><a><router-link to="/logout">Logout</router-link></a></li>
</ul>


<a href="" class="btn"><span>+ Post Video</span></a>


</div>
</div>
</div>
</template>



<script>
</script>


<style scoped>
#nav {
text-align: center;
}

.nav_inner {
    height: 90%;
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
    width:100%;
    height:100%;
    position:relative;
}


ul {
    list-style:none;
    margin-top: 30px;
}

li {
    margin-top: 20px;
}

#profile_pic {
    width: 120px;
    border-radius:100vh;
    margin-top:10px;
}

#logo {
    width:140px;
}


.btn { 
    width:140px;
    display: inline-block;
    color: white !important;
    padding-top: 12px;
    padding-bottom: 12px;
    border-radius:100vh;
    text-decoration: none;
    outline: none;
    /*背景の色と形状*/
    background: linear-gradient(270deg, #FFDD83 0%, #CF2E92 100%);
    background-position: 1% 50%;
    background-size: 130% auto;
    /*アニメーションの指定*/
    transition: all 0.3s ease-out;
    position: absolute;
    top: 90%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
}

.btn:hover {
    color: #fff;
    background-position: 99% 50%;
}
</style>