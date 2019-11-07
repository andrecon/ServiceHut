var app4 = new Vue({
    el: '#app-4',
    data: {
      postdata: [],
      seen:true,
      unseen:false
    },
    //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
    created: function() {
          this.fetchPostsList();
          this.timer = setInterval(this.fetchPostsList, 10000);
    },
    methods: {
        fetchPostsList: function() {
          axios
            .get('/postdata/')
            .then(response => (this.postdata = response.data.events))
          console.log(this.postdata)
          this.seen=false
          this.unseen=true
      },
      cancelAutoUpdate: function() { clearInterval(this.timer) }
    },
    beforeDestroy() {
      // clearInterval(this.timer)
      this.cancelAutoUpdate();
    }
  
  })