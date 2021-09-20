<template>
    <div>
        <Card :posts="postsList" types="home" @openCommentModal="openCommentModal"/>
    </div>
</template>

<script>
import Card from './Card'
import {db} from '../firebase'
import { collection, query, getDocs } from "firebase/firestore";
import { postObj } from "./type/postObj"

export default {
    name: 'Home',
    data() {
      return {
        postsList:[]
      }
    },
    components: {
        Card
    },
    methods: {
      getPostData: async function(){
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
          this.postsList.push(obj)
        });
      },
      openCommentModal:function(info){
        this.$emit("openCommentModal",info);
      }
    },
    mounted: function() {
      this.getPostData()
      this.$emit("change")
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