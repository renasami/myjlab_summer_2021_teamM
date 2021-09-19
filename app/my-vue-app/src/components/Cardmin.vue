<template>
    <div class="cardmin">
            <iframe @click="sambnail = !sambnail"
            v-if="sambnail" 
            class='upper_video'
            width="120%" 
            height="150%" 
            v-bind:src="url"
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write;
            encrypted-media; gyroscope; 
            picture-in-picture" allowfullscreen></iframe>
            <div v-else
            @click="sambnail = !sambnail"
            class='upper_video'
            width="100%" 
            height="100%" 
            v-bind:src="url"
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write;
            encrypted-media; gyroscope; 
            picture-in-picture" allowfullscreen>
                <img v-bind:src="youtube"
                width="70%" 
                height="50%"/>
            </div>                
        <div class='lower_text'>
            <div class="title">{{ title }} </div>
            <div class="sub-title">{{ caption }}</div>
            <div class="line"></div>

            <div class="icon">
                <div class='like_button'>
                    <button @click="buttonState = !buttonState"><svg v-bind:class="{ after_button: buttonState }"  xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></button>
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#231815" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                </div>
                </div>
        </div>
        
    </div>
</template>
<script>
//
 export default {
    name: 'Cardmin',
    data(){
        return{
            buttonState:false,
            sambnail : false,
        }
    },
    method:{
        //いいねで変更
        changeState:function(index){
            console.log('Change state')
            this.buttonState[index] = !this.buttonState;
        }
    },
    props:  ["id","uid","title","caption","url","likedNumber"],
    mounted: function() {
    // <p>Hello</p>が出力される
    console.log(this.$refs);
    console.log(this.$$refs.id)
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
  height:300px;
  margin: 20px 20px;
  display: inline-block;
  /* box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2); */
  border-radius: 3px;
}
.cadmin {
    display: flex;
  flex-direction: column;
}

.cards_inner {
  margin: 0 auto;
  width:95%;
  height:95%;
}

.upper_video {
  width:100%;
  background-color:#F7F7F7;
  /* box-shadow: 0px 2px 3px 0 rgba(0,0,0,0.1); */
  /* border-radius: 3px; */
}

.lower_text {
  width:90%;
  margin: auto;
  /* display: flex;
  justify-content: space-between; */
}
button {
    border: none;
    background-color: transparent;
}


.title {
  font-size: 1.2em;
  margin-bottom: 5px;
  text-align: left;
}

.sub-title {
    font-size: 0.8em;
    color: rgb(116, 116, 116);
    width:95%;
    margin-bottom: 15px;
    text-align: left;
}

.line {
    width:100%;
    height:1px;
    background-color: rgb(212, 212, 212);
}

.icon {
    margin: auto;
}

.icon svg {
    margin:10px 0;
    padding: 0 2px;
}


.after_button {
  fill: #E36C9E;
  stroke: #E36C9E;
}


</style>