<template>
<div>

    <!-- モバイル用 -->
    <div class="hamburger-menu">
        <input type="checkbox" id="menu-btn-check">
        <label for="menu-btn-check" class="menu-btn"><span></span></label>
        <div class="menu-content">
            <ul>
                <li>
                    <a><router-link to="/home"><span class='router_box'><span class='router_text'>Home</span></span></router-link></a>
                </li>
                <li>
                    <a><router-link to="/like"><span class='router_box'><span class='router_text'>Repeat Likes</span></span></router-link></a>
                </li>
                <li>
                    <a><router-link to="/profile"><span class='router_box'><span class='router_text'>Profile</span></span></router-link></a>
                </li>
                <li class="log-padding">
                    <a @click="logout" ><span class='router_box'><span class='router_text'>Logout</span></span></a>
                </li>
            </ul>
        </div>
        <div class="mobile-post" @click="createModal">＋</div>
    </div>
    <!-- モバイル用 -->


    <div id='nav'>
    <div class='nav_inner'>
    <div class='nav_inner2'>


    <img id='logo' alt="VG logo" src="./img/vglogo.svg"><br>
    <img id='profile_pic' alt="Profile pic" src="./img/Profile.png">
    <h3>{{ username }}</h3>

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
</div>
</template>



<script>
import store from "../store"
import { getAuth, signOut } from "firebase/auth";
import {toStore} from '../scripts/userInfoToStore'

export default {
    data(){
        return{
            username:''
        }
    },
  methods: {
    createModal(){
      this.$emit('createModal')
    },
    logout(){
        const auth = getAuth()
        signOut(auth).then().catch(err=>{alert(err)});
        store.commit("setIsLogin",false);
        store.commit("setUserId",null);
        store.commit("setUsername",null);
        this.$emit("closeModal")
        this.$router.push("/login")
        location.reload()
    }
  },
  mounted: function() {
    toStore()
    this.username = store.state.user
  } 
}

</script>


<style scoped>
#nav {
text-align: center;
display: none;
}

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


/* モバイルメニュー */
.menu-btn {
    position: fixed;
    top: 10px;
    right: 10px;
    display: flex;
    height: 40px;
    width: 40px;
    justify-content: center;
    align-items: center;
    z-index: 90;
}
.menu-btn span,
.menu-btn span:before,
.menu-btn span:after {
    content: '';
    display: block;
    height: 3px;
    width: 25px;
    border-radius: 3px;
    background-color: #F8D371;
    position: absolute;
}
.menu-btn span:before {
    bottom: 8px;
}
.menu-btn span:after {
    top: 8px;
}
#menu-btn-check:checked ~ .menu-btn span {
    background-color: rgba(255, 255, 255, 0);/*メニューオープン時は真ん中の線を透明にする*/
}
#menu-btn-check:checked ~ .menu-btn span::before {
    bottom: 0;
    transform: rotate(45deg);
    background-color:#ffffff;
}
#menu-btn-check:checked ~ .menu-btn span::after {
    top: 0;
    transform: rotate(-45deg);
    background-color:#ffffff;
}
.menu-content ul {
    padding: 70px 10px 0;
}
.menu-content ul li {
    border-bottom: solid 1px #ffffff;
}
.menu-content ul li a {
    display: block;
    width: 100%;
    font-size: 15px;
    font-weight: bold;
    box-sizing: border-box;
    color:#ffffff;
    padding: 9px 15px 10px 0;
    position: relative;
}
.menu-content {
    width: 50%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 100%;/*leftの値を変更してメニューを画面外へ*/
    z-index: 10;
    background-color: #F8D371;
    transition: all 0.5s;/*アニメーション設定*/
}
#menu-btn-check:checked ~ .menu-content {
    left: 50%;/*メニューを画面内へ*/
}
#menu-btn-check {
    display: none;
}
.log-padding{
    padding: 9px 0;
}
.mobile-post{
    position:fixed;
    bottom: 20px;
    right: 20px;
    color:white;
    background-color: #F8D371;
    width: 50px;/*幅*/
	height: 50px;/*高さ*/
	border-radius: 50%;/*角丸*/
    font-weight: bold;
    font-size: 1.8em;
    vertical-align: middle;
    display: flex;
    justify-content: center;
    align-items: center;

}
/* モバイルメニュー */

@media (min-width: 960px) {
/*********************************************************
  Stylesheet: 960px以上のタブレットやモニタで適用
*********************************************************/
.hamburger-menu{
    display: none;
}
#nav{
    display: block;
}

}
</style>