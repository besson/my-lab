(function() {

  window.Tweet = Backbone.Model.extend({
  });

  window.Tweets = Backbone.Collection.extend({
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

}());

