<template>
<div id='nav'>
<div id='nav_inner'>
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
</template>



<script>
</script>


<style scoped>
#nav_inner {
    height: 80vh;
    margin: 0 auto;
}

ul {
    list-style:none;
}

li {
    margin-top: 20px;
}

#profile_pic {
    width: 120px;
    border-radius:100vh;
}

#logo {
    width:140px;
}

.btn {
    display: inline-block;
    color:#fff;
    padding: 10px 30px;
    border-radius:100vh;
    text-decoration: none;
    outline: none;
    /*背景の色と形状*/
    background: linear-gradient(270deg, #CF2E92 0%, #FFDD83 100%);
    background-position: 1% 50%;
    background-size: 200% auto;
    /*アニメーションの指定*/
    transition: all 0.3s ease-out;
}

.btn:hover {
    color: #fff;
    background-position: 99% 50%;
}
</style>