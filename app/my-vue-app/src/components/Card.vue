<template>
<div class="card">
    <div v-for="(items, index) in groupedArray" :key="index">
        <li class='cards' v-for="item in items" :key="item.id">
        <div class='cards_inner'>

        <div class='upper_video'>{{ item.thumbnail }}</div>

        <div class='lower_text'>
          <div class="title">{{ item.title }}</div>
          <div class="icon">
            <div class='like_button'>
                <svg v-bind:class="{ after_button: buttonState }" v-on:click="changeState" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
              </div>
            </div>
        </div></div>
        </li>
    </div>
</div>
</template>

<script>
import axios from 'axios';
axios.get('http://0.0.0.0:8000/latestposts').then(result => console.log(result.data))

export default {
     name: 'Card',
   data: function () {
     return {
        list: [],
        buttonState: false  
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
methods:{
  changeState: function(){
       
          //  いいねがクリックされた後の処理

    this.buttonState = !this.buttonState
  }
},
mounted: function(){
            // axiosでデータの受け渡し
            this.axios.get('http://0.0.0.0:8000/latestposts').then(response => 
             {
               const movies = response.data
               movies.forEach(response => this.list.push({
                 thumbnail: response["THUMBNAIL_ID"],
                 title: response["TITLE"]
               }))
             })
             .catch((e) => {
            alert(e);
          });
          console.log(typeof(this.list))
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
  height:250px;
  margin: 20px 20px;
  display: inline-block;
  /* box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2); */
  border-radius: 3px;
}

.cards_inner {
  margin: 0 auto;
  width:95%;
  height:95%;
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