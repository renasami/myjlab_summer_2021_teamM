import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios' //追記
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify' 




Vue.config.productionTip = false


// let functions = firebase.default.app().functions("asia-northeast1");
// let db = firebase.default.firestore();


Vue.use(VueAxios, axios)
Vue.use(Vuetify)


new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
});
