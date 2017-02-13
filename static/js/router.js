$(function() {
    // Router configuration
    var app = $.sammy('#container', function() {
        this.use('Template')

        // Index
        this.get('#/sensor/:sensor', function(context) {
            context.render('/sensor/' + this.params.sensor + '.html')
                .replace(context.$element());
        })     

        // Configuration
        this.get('#/config', function(context) {
            context.render('/static/html/config.html')
                .replace(context.$element())
        })
        
        // 404
        this.get('#/.*', function(context) { 
            this.render('/static/html/errors/404.html')
                .replace(context.$element())
        })
    })

    // Initialize router
    $(function() { app.run('#/') })
})
