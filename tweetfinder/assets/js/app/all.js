(function() {

  window.app = {model: {}, collection: {}, view: {}};

  app.model.Tweet = Backbone.Model.extend({
  });

  app.collection.TweetList = Backbone.Collection.extend({
    model: app.model.Tweet,
    parse: function(response) {
      return response.results;
    },
    getTweets: function(searchKey) {
      this.url = "http://search.twitter.com/search.json?callback=?&q=" + searchKey
    }
  });

  app.view.TweetView = Backbone.View.extend({
    el: $("#tweets"),

    render: function(){
      var content = "<li>" + this.model.get("text") + "</li>";
      $("#tweets").append(content);
    }
  });

  app.view.TweetListView = Backbone.View.extend({
    el: $("#tweets-container"),

    initialize: function(){
      this.collection.on("reset", this.render, this);
    },

    render: function(){
      $("#tweets").html("");
      this.collection.each(this.addOne, this);
    },

    addOne: function(tweet){
      var tweetView = new app.view.TweetView({model: tweet});
      tweetView.render();
    }
  });

  app.view.TweetFinder = Backbone.View.extend({

    render: function() {
      var tweetList = new app.collection.TweetList();
      var tweetListView = new app.view.TweetListView({collection: tweetList});

      $("#search-submit").click(function(e) {
        e.preventDefault();
        tweetList.getTweets($("#search-key").val());
        tweetList.fetch({
          success: function() {
            tweetListView.render();
          }});
      });

      setInterval(function() {tweetList.fetch();}, 4000);
    }
  });

}());

