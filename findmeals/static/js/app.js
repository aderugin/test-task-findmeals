var app = angular.module('Search', []);


app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});


app.controller('SearchController', function($scope, $http) {
    $scope.form = {};
    $scope.submitForm = (function() {
        $http.get('/ajax/search/?' + $('.js-form').serialize())
            .success(function(data, status, headers, config) {
                $scope.recipes = data.recipes;
            })
            .error(function(data, status, headers, config) {
            }); 
    });
});



$(document).ready(function() {
    $('.js-autocomplete').autocomplete({
        paramName: 'q',
        serviceUrl: '/ajax/ingredient_autocomplete/',
        onSelect: function (suggestion) {
            var isInclude = $(this).is('.js-autocomplete-include') ? true : false,
                appendObj = isInclude ? $('.js-include') : $('.js-exclude'),
                labelClass = isInclude ? 'label-success' : 'label-warning',
                inputName = isInclude ? 'include' : 'exclude',
                ngModel = isInclude ? 'ng-model="form.include"': 'ng-model="form.exclude"';

            appendObj.append('<input ' + ngModel + ' type="hidden" value="' + suggestion.data +
                             '" name="' + inputName + '" />')

            $(this).val('');
            $('.js-ingredients').append('<span data-id="' + suggestion.data + 
                                        '" class="js-ingredient-label label ' + labelClass + 
                                        '">' + suggestion.value + ' <a href="#">x</a></span> ');
        }
    });


    $(document).on('click', '.js-ingredient-label a', function(event) {
        event.preventDefault();

        if ($(this).parent().is('.label-success')) {
            $('.js-include').find('[value="' + $(this).parent().data('id') + '"]').remove();
            $(this).parent().remove();
        } else {
            $('.js-exclude').find('[value="' + $(this).parent().data('id') + '"]').remove();
            $(this).parent().remove();
        };
    });
});