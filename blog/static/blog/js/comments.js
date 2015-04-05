var comments = angular.module('comments', []).
    config([
        '$httpProvider',
        '$interpolateProvider',
        function($httpProvider, $interpolateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
            $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        }]);