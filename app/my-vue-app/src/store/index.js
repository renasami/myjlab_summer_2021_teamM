import Vuex from 'vuex'
import Vue from 'vue'


Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
      user:'',
    },
    methods: {
        user (state,user) {
            state.user = user;
        },
        logOut (user) {
            this.user = null;
        }
    }
  })

export default store