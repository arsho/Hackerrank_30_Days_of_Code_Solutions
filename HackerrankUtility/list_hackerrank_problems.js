// https://www.hackerrank.com/domains/tutorials/30-days-of-code
$ar = []
$('.challengecard-title').each(function(){
   $title = $(this).children().remove().end().text().trim();
   $ar.push($title);
})
console.log($ar);
copy($ar);
