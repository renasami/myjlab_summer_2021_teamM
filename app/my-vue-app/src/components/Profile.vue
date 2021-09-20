<template>
<div class='profile'>
     <div class="profile_inner">
         <img class='profile_img' src="./img/Profile.png"><br>
         <h3>{{ username }}</h3>
         <input type="text" id="name" name="name" placeholder="User Name"><br>
         <input type="text" id="password" name="name" placeholder="Password"><br>
         <input type="text" id="image" name="name" placeholder="new Image URL"><br>
         <a href="" class="btn"><span>完了</span></a>
     </div>
</div>
</template>

<script>
import store from "../store"
import { db } from '../firebase'
import {getDocs,where,collection,query} from 'firebase/firestore'

export default {
    name: "Profile",
    data() {
        return {
            username:"",
            fas:"fas",
            imgsrc: "",
        }
    },
    methods: {
        changeUserImage:async function(){
            const q = query(collection(db,'videogram/v1/users'),where("uid","==",store.state.userId))
            const docs = await getDocs(q)
            if(docs.empty || docs.docs[0].image == undefined) return
            store.commit("setState","imgsrc",docs.docs[0].image)
            this.imgsrc = docs.docs[0].image
        }
    },
    mounted: function() {
        this.changeUserImage()
        this.username = store.state.user
    }

}
</script>

<style scoped>
.profile {
  width:100%;
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
#image {
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

@media (min-width: 960px) {
/*********************************************************
  Stylesheet: 960px以上のタブレットやモニタで適用
*********************************************************/
.profile{
    width:80%;
}
}
</style>
