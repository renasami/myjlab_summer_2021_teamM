<template>
<div class="card">
<component-children v-bind:variable="list" />
    <div v-for="(items, index) in groupedArray" :key="index">
        <li class='cards' v-for="item in items" :key="item.id">
          <div class='cards_inner'>
          <Cardmin v-bind:ttl="item" :index="item.id" :url="item.url" :youtube="item.youtube_id" />    
          </div>
        </li>
    </div>
    
</div>
</template>

<script>
import Cardmin from './Cardmin.vue'
//import axios from 'axios';
//axios.get('http://0.0.0.0:8000/latestposts').then(result => console.log(result.data))

export default {
    name: 'Card',
    components: {
      Cardmin
    },
   data: function () {
     return {
        list: [],
     }
   },
  computed: {
    groupedArray() {
      const base = this.list.length
      const split_cnt = 3       // 何個ずつに分割するか
      const grouped_list = []
      for (let i=0; i<Math.ceil(base/split_cnt); i++) {
        let multiple_cnt = i * split_cnt  // 3の倍数
        // (i * 3)番目から(i * 3 + 3)番目まで取得
        let result = this.list.slice(multiple_cnt, multiple_cnt + split_cnt) 
        grouped_list.push(result)
      }
      return grouped_list
    }
  },
  
  mounted: function(){
        if(location.pathname == "/like"){
          let cookies = document.cookie; //全てのcookieを取り出して 
          let cookiesArray = cookies.split(';'); // ;で分割し配列に
          let uid 
          let likedList
          for(var c of cookiesArray){
            let cArray = c.split('=')
            if(cArray[0] == ' userid'){ 
              uid = cArray[1]
            }
          }
        this.axios.get('http://0.0.0.0:8000/get_URL').then(response => {
          this.list = response.data
          console.log(response.data)
          })
        .catch((e) => {
        alert(e);
      });
      this.axios.get(`http://0.0.0.0:8000/users/${uid}/likes`).then(response => {
        response.data.forEach(res => {
          for(var n = 0; n < this.list.length; n++){
            if(this.list[n].movie_id == res.POST_ID){
              likedList.push(this.list[n])
            }
          }
        }); 
        this.list = likedList
        console.log(this.list)
    })} else{
      this.axios.get('http://0.0.0.0:8000/get_URL').then(response => {
          this.list = response.data
          console.log(response.data)
          })
        .catch((e) => {
        alert(e);
      });
        
     }
    }
  }




</script>

<style scoped>
.card {
  width:80%;
  position: absolute;
  right: 0;
  margin-top: 50px;
}

.cards {
  width:320px;
  margin: 20px 20px;
  display: inline-block;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
  background-color: white;
  cursor: pointer;
  transition-duration: 0.4s;
}

.cards:hover{
        transform: scale(1.1);
        transition-duration: 0.4s;
      }

.cards_inner {
  margin: 0 auto;
}

.upper_video {
  width:100%;
  height:75%;
  background-color:#F7F7F7;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
}

.lower_text {
  width:100%;
  height:25%;
  margin-top:10px;
  display: flex;
  justify-content: space-between;
}

.title, .icon {
  display: inline-block;
}

.title {
  font-size: 1.2em;
}

.after_button {
  fill: #E36C9E;
  stroke: #E36C9E;
}

.like_button {
  float: left;
}

</style>