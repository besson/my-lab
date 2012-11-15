(function() {

  window.Tweet = Backbone.Model.extend({
  });

  window.TweetList = Backbone.Collection.extend({
    model: window.Tweet,
    parse: function(response) {
      return response.results;
    },
    getTweets: function(searchKey) {
      this.url = "http://search.twitter.com/search.json?callback=?&q=" + searchKey
    }
  });

  window.TweetView = Backbone.View.extend({
    el: $("#tweets"),

    render: function(){
     var content = "<li>" + this.model.get("text") + "</li>";
      $("#tweets").append(content);
    }
  });

  window.TweetListView = Backbone.View.extend({
    el: $("#tweets-container"),

    initialize: function(){
      this.collection.bind("reset", this.render, this);
    },

    render: function(){
      $("#tweets").html("");
      this.collection.each(this.addOne, this);
    },

    addOne: function(tweet){
     var tweetView = new window.TweetView({model: tweet});
     tweetView.render();
    }
  });

}());

