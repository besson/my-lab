(function() {

  window.Tweet = Backbone.Model.extend({
  });

  window.TweetList = Backbone.Collection.extend({
    model: window.Tweet,
    url: "http://search.twitter.com/search.json?callback=?&q=corinthians",
    parse: function(response) {
      return response.results;
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

    render: function(){
      this.collection.each(this.addOne, this);
    },

    addOne: function(tweet){
     alert(tweet);
     var tweetView = new window.TweetView({model: tweet});
     tweetView.render();
    }
  });

}());

