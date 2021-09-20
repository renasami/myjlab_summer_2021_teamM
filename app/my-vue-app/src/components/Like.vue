<template>
    <div>
        <Card types="like"  @openCommentModal="openCommentModal" :posts="likedPostList"/>
    </div>
</template>
<script>
import Card from './Card.vue'
import store from '../store'
import {db} from '../firebase'
import { collection, query, getDocs, where } from "firebase/firestore";
import { postObj } from "./type/postObj"

export default {
    name:"Like"  ,
    components:{
        Card
    },
    data(){
        return{
            likedPostList: [],
            likedIdList:[]
        }
    },
    methods:{
        openCommentModal:function(info){
        this.$emit("openCommentModal",info);
      },
      getPostData: async function(){
        let postData = []
        const posts = collection(db, "videogram/v1/posts");
        const q = query(posts)
        const querySnapshot = await getDocs(q);
        querySnapshot.forEach((doc) => {
          const obj = new postObj(doc.id, 
                        doc.data().userId.id,
                        doc.data().title,
                        doc.data().caption,
                        doc.data().url,
                        doc.data().likedNumber)
          postData.push(obj)
        });
        
        this.likedIdList.forEach((liked) =>{
            postData.forEach((post)=>{
                if(post.id == liked) this.likedPostList.push(post)
            })
        })
      },
    },  
    mounted:async function() {
      const q = query(collection(db,"videogram/v1/users"),where("uid","==",store.state.userId))
      await getDocs(q).then(ret =>ret.docs[0]).then(res => {this.likedIdList = res.data().like})
      this.getPostData()
    }
}

</script>
<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #231815;
  margin-top: 0px;
  height: 100vh;
}

#nav {
  position: fixed;
  background-color: #F7F7F7;
  top:0;
  width:20%;
  height:100vh;
}

#nav a {
  color: #231815;
}
</style>