# Try alternate locators if one fails.
# Reduce failures caused by UI changes.

from selenium.common.exceptions import NoSuchElementException

def find_element_self_healing(driver, locators):
    for locator in locators:
        try:
            return driver.find_element(*locator)
        except NoSuchElementException:
            continue

    raise NoSuchElementException("Element not found using any fallback locator")