var gulp = require('gulp');
var gutil = require('gulp-util');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var runSequence = require('run-sequence');
var browserSync = require('browser-sync').create();

gulp.task('sass', function() {
	return gulp.src('./assets/css/master.sass')
		.pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
		.pipe(concat('master.min.css'))
		.pipe(gulp.dest('./assets/css/'))
		.pipe(browserSync.stream());
});

gulp.task('js', function() {
	browserSync.reload();
});

gulp.task('html', function() {
	browserSync.reload();
});

//watch files
gulp.task('watch', ['browserSync', 'build'], function() {
	gulp.watch('./assets/css/**/*.sass', ['sass']);
	gulp.watch('./assets/js/*.js', ['js']);
	gulp.watch('./templates/**/*.html', ['html']);
	gulp.watch('./viewer/templates/**/*.html', ['html']);
	gulp.watch('./joins/templates/**/*.html', ['html']);
});

//browser sync
gulp.task('browserSync', function() {
	browserSync.init({
		baseDir: "./",
		proxy: "http://localhost:8000/",
		startPath: "/",
		browser: ['chrome']
	})
});

gulp.task('default', ['watch']);

gulp.task('build', function(callback) {
	runSequence(['sass'], callback)
});