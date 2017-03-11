// grab our gulp packages
const gulp  = require('gulp'),
      gutil = require('gulp-util'),
      concat = require('gulp-concat'),
      babel = require('gulp-babel'),
      sass = require('gulp-sass');

const merge = require('merge-stream');

const css_packages = [
  'node_modules/normalize.css/normalize.css'
]

gulp.task('js', () =>
    gulp.src('serve/js/**/*.js')
        .pipe(babel({
            presets: ['es2015']
        }))
        .pipe(concat('app.js'))
        .pipe(gulp.dest('src/static/js'))
);

gulp.task('scss', function () {
  return merge(
              gulp.src(css_packages)
                .pipe(concat('import.css')),
              gulp.src('serve/css/**/*.scss')
                .pipe(concat('app.scss'))
                .pipe(sass().on('error', sass.logError))
            ).pipe(concat('app.css'))
             .pipe(gulp.dest('src/static/css'));
});


gulp.task('scss:watch', function () {
  gulp.watch('serve/scss/**/*.scss', ['scss']);
});

gulp.task('js:watch', function () {
  gulp.watch('serve/js/**/*.js', ['js']);
});


// default
gulp.task('default', [ 'js', 'scss', 'scss:watch', 'js:watch'], function() {
  return gutil.log('Gulp is running!')
});

// production task
gulp.task('production', [ 'js', 'scss' ], function() {
  return gutil.log('Compiled everything!')
});
