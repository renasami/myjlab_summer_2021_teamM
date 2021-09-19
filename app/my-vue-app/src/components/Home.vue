<template>
    <div>
        <Card :posts="postsList" />
    </div>
</template>

<script>
import Card from './Card'
import {db} from '../firebase'
import { collection, query, getDocs } from "firebase/firestore";
function postObj(id,uid,title,caption,url,likedNumber){
  this.id = id;
  this.uid = uid;
  this.title = title;
  this.caption = caption;
  this.url = url;
  this.likedNumber = likedNumber;
}

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
      }
    },
    mounted: function() {
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