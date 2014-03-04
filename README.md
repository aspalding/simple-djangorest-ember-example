simple-djangorest-ember-example
===============================

This example utilizes the [django-rest-framework](http://www.django-rest-framework.org/) and [ember-data-django-rest-adapter](https://github.com/toranb/ember-data-django-rest-adapter) to build on the [todomvc example](http://emberjs.com/guides/getting-started/) provided by the ember.js docs. The REST service provides networked, persistance storage for the application. 

To try this out, you should complete the ember.js todomvc tutorial. Then change the following lines located in application.js as follows.

    Todos.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
      host: 'http://localhost:8080', //The address:port of your Django Rest application.
    });