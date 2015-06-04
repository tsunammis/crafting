# Show private services
php app/console container:debug --show-private

# Show translation for one Bundle
php app/console translation:debug --domain="messages" en IliusUnloggedBundle

# Install vendors and optimize it
php composer.phar install --no-dev --optimize-autoloader

# Empty cache and warmup
php app/console cache:clear --env=prod --no-debug

# Install assets with assetic
php app/console assetic:dump --env=prod --no-debug

# Install assets
php app/consolle assets:install web/static
