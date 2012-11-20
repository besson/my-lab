  window.app = {model: {}, collection: {}, view: {}}

  class app.model.Tweet extends Backbone.Model

  class app.collection.TweetList extends Backbone.Collection

    model: app.model.Tweet
    parse: (response) ->
      response.results
    getTweets: (searchKey) ->
      @url = "http://search.twitter.com/search.json?callback=?&q=" + searchKey

  class app.view.TweetView extends Backbone.View

    el: $("#tweets")
    render: ->
      content = "<li>" + this.model.get("text") + "</li>"
      $("#tweets").append(content)

  class app.view.TweetListView extends Backbone.View

    el: $("#tweets-container")
    initialize: ->
      @collection.on("reset", this.render, this)
    render: ->
      $("#tweets").html("")
      @collection.each(this.addOne, this)
    addOne: (tweet) ->
      tweetView = new app.view.TweetView({model: tweet})
      tweetView.render()

  class app.view.TweetFinder extends Backbone.View

    render: ->
      tweetList = new app.collection.TweetList()
      tweetListView = new app.view.TweetListView({collection: tweetList})

      $("#search-submit").click (e) ->
        e.preventDefault()
        tweetList.getTweets($("#search-key").val())
        tweetList.fetch
          success: ->
            tweetListView.render()

      setInterval ->
        tweetList.fetch()
      , 4000

