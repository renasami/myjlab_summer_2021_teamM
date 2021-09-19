import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios' //追記
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify' 
import { initializeApp } from 'firebase/app';


Vue.config.productionTip = false

const firebaseConfig = {
  apiKey: "AIzaSyAhPERjK_3C8mZGlmLKAe6N8WO0P1tHqvE",
  authDomain: "myjlab-summer-tem-m.firebaseapp.com",
  projectId: "myjlab-summer-tem-m",
  storageBucket: "myjlab-summer-tem-m.appspot.com",
  messagingSenderId: "917822943614",
  appId: "1:917822943614:web:be518919882849e5fd432f",
  measurementId: "G-02LZZZ2LK1"
};

initializeApp(firebaseConfig);

// let functions = firebase.default.app().functions("asia-northeast1");
// let db = firebase.default.firestore();



console.log('fas')
Vue.use(VueAxios, axios)
Vue.use(Vuetify)


new Vue({
  el: '#app',
  router,
  render: h => h(App),
});
