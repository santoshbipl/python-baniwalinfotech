<?php
/**
 * The template for displaying the footer
 *
 * Contains the closing of the #content div and all content after.
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package baniwal
 */

?>

	<footer id="colophon" class="site-footer">
		
	</footer><!-- #colophon -->
</div><!-- #page -->

<?php wp_footer(); ?>
<script type="text/javascript" src="assets/js/bootstrap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/js/all.min.js" integrity="sha512-1JkMy1LR9bTo3psH+H4SV5bO2dFylgOy+UJhMus1zF4VEFuZVu5lsi4I6iIndE4N9p01z1554ZDcvMSjMaqCBQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
 <script type="text/javascript"src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>


<script type="text/javascript">
  const number = document.querySelectorAll('.number')
  let intervel = 500;

  number.forEach((num)=>{
    let starValue = 0;
    let endValue = parseInt(num.getAttribute('data-target'));
    let duration = Math.floor(intervel / endValue);
    let counter = setInterval(function(){
      starValue += 1;
      num.textContent = starValue;
      if(starValue == endValue){
        clearInterval(counter)
      }
    }, 50)

    console.log(num)
  })

</script>

<script type="text/javascript">
	$(document).ready(function () {
        $(".slider").slick({
          infinite: true,
          slidesToShow: 3,
          slidesToScroll: 1,
          speed: 500,
          autoplaySpeed: 5000,
          infinite: true,
          autoplay: true,
          centerMode: true,
          centerPadding: "0",
        });
      });
</script>






</body>
</html>
