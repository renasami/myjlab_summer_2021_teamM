<template>
<div id='nav'>
<div class='nav_inner'>
<div class='nav_inner2'>


<img id='logo' alt="VG logo" src="./img/vglogo.svg"><br>
<img id='profile_pic' alt="Profile pic" src="./img/Profile.png">
<h3>Yutaka Miyaji</h3>

<ul>
            <li><a><router-link to="/home"><span class='router_box'><span class='router_text'>Home</span></span></router-link></a></li>
            <li><a><router-link to="/like"><span class='router_box'><span class='router_text'>Like</span></span></router-link></a></li>
            <li><a><router-link to="/profile"><span class='router_box'><span class='router_text'>User Profile</span></span></router-link></a></li>
            <li><a><span class='router_box'><span class='router_text'>Logout</span></span></a></li>
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
    margin-left: 40px;
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
    margin-top: 50px;
}

li {
    margin-top: 20px;
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