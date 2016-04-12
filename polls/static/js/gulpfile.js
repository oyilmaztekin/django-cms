var gulp = require('gulp'),					
	size = require('gulp-filesize'),
	connect = require('gulp-connect'),	
	watch = require('gulp-watch'),	
  stylus = require('gulp-stylus'),
	jade = require('gulp-jade');


var stylSources = ['styl/main.styl']
var exportStyl = '../build/css/';

//live reload
gulp.task('connect', function() {
  connect.server({
    root: '../build/',
    livereload: true,
    port: 8000
  });
});

//html
gulp.task('html', function () {
  gulp.src('*.jade')
  	.pipe(size())   
  	.pipe(jade( {pretty:true}))    
  	//.pipe(uglify())	 	
  	.pipe(gulp.dest('../build/'))
    .pipe(connect.reload());
});


//js
gulp.task('js',function(){
	gulp.src('**/*.js')		
		.pipe(size())
		.pipe(gulp.dest('../build/js/'))
		.pipe(connect.reload());
})

gulp.task('stylus', function () {
  gulp.src(stylSources)
  	.pipe(size())
    .pipe(stylus())
    .pipe(gulp.dest(exportStyl))
    .pipe(connect.reload());
});

//watch
 gulp.task('watch', function () {
  gulp.watch(['jade/*.jade']);  
  gulp.watch(['*.jade'], ['html']);
  gulp.watch(['js/*.js'], ['js']);  
  gulp.watch([stylSources],['stylus']);
});

gulp.task('default',['connect','watch','html','stylus','js']);