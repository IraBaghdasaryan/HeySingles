from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class WelcomePageLocators:
    _joinus_button = {"by": By.ACCESSIBILITY_ID, "value": "welcomeLoginButton"}
    _login_button = {"by": By.ACCESSIBILITY_ID, "value": "welcomeRegistrationButton"}


class LoginPageLocators:
    _username_input = {"by": By.ACCESSIBILITY_ID, "value": "signInUsernameInput"}
    _password_input = {"by": By.ACCESSIBILITY_ID, "value": "signInPasswordInput"}
    _seepassword_button = {"by": By.ACCESSIBILITY_ID, "value": "signInPasswordInputEye"}
    _signin_button = {"by": By.ACCESSIBILITY_ID, "value": "signInLoginButton"}
    _back_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _facebook_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _vk_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _forgot_password_button = {"by": By.ACCESSIBILITY_ID, "value": "signInForgetPassword"}
    _signup_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _hs_logo = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _wrong_username = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _wrong_pass = {"by": By.ACCESSIBILITY_ID, "value": ""}


class SwipePageLocators:
    _photo_ = {"by": By.ACCESSIBILITY_ID, "value": "cardUserImage"}
    _dislike_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeDislikeIcon"}
    _gift_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeGiftIcon"}
    _like_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeLikeIcon"}
    _filter_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeFilterIcon"}
    _undo_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeUndoIcon"}
    _location_value = {"by": By.ACCESSIBILITY_ID, "value": "userCardLocationValue"}
    _block_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardBlockOrReport"}
    _gift_card_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardSendGiftCardButtonText"}
    _user_name = {"by": By.ACCESSIBILITY_ID, "value": "cardUserFirstName"}
    _user_age = {"by": By.ACCESSIBILITY_ID, "value": "cardUserAge"}
    _report_abuse_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardReportAbuseButton"}
    _report_block_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardReportAbuseButton"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardBlockOrReportCancelButton"}

class IDlocators:
    _user_Id = {"by":By.ACCESSIBILITY_ID, "value": 	"reportAbuseScreenUserId"}

class BlocorReport:
    _report_abuse_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardReportAbuseButton"}
    _block_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardBlockUnblockButton"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardBlockOrReportCancelButton"}


class MenuLocators:
    _search_button = {"by": By.XPATH,  "value": "//android.widget.FrameLayout[@content-desc=\"Search, tab, 1 out of 4\"]/android.widget.TextView"}
    _swipe_button = {"by": By.XPATH, "value": "//android.widget.FrameLayout[@content-desc=\"Search, tab, 1 out of 4\"]/android.widget.TextView"}
    _chat_button = {"by": By.XPATH, "value": "//android.widget.FrameLayout[@content-desc=\"Chat, tab, 3 out of 4\"]/android.widget.ImageView"}
    _me_button = {"by": By.XPATH, "value": "//android.widget.FrameLayout[@content-desc=\"Me, tab, 4 out of 4\"]/android.widget.TextView"}



class SwipeFilterLocator:
    _save_button = {"by": By.ACCESSIBILITY_ID, "value": "filterHeaderCheckIcon"}
    _show_men_button = {"by": By.ACCESSIBILITY_ID, "value": "filterGenderButtonMen"}
    _show_women_button = {"by": By.ACCESSIBILITY_ID, "value": "filterGenderButtonWomen"}
    _show_both_button = {"by": By.ACCESSIBILITY_ID, "value": "filterGenderButtonBoth"}
    _location_button = {"by": By.ACCESSIBILITY_ID, "value": "filterLocationInputField"}



class SwipeLocationLocators:
    _search_box = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteSearchInput"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteCancel"}
    _current_location = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteCurrentLocationRow"}
    _line_results = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteCurrentLocationRow"}



class MyProfile:
    _settings_button = {"by": By.ACCESSIBILITY_ID, "value": "mainProfileSettingsIcon"}
    _need_help_button = {"by": By.ACCESSIBILITY_ID, "value": "//android.view.View[@content-desc=\"%3Fgclid%3DEAIaIQobChMIm8_bjYPY7wIVCca7CB1OOAP5EAEYASAAEgKyzPD_BwE\"]/android.view.View"}
    _credits_number = {"by": By.XPATH, "value": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.TextView[1]"}


class Settings:
    _basic_info_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemBasic Info"}
    _fb_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemJoin HeySingles on Facebook"}
    _help_centre_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemHelp center"}
    _report_problem_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemReport a problem"}
    _account_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemAccount"}
    _linked_account_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemLinked Accounts"}
    _notifications_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemNotifications"}
    _privacy_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemPrivacy"}
    _invisible_mode_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemInvisible mode"}
    _verification_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemVerifications"}
    _payment_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemPayment Settings"}
    _language_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemApp Language"}
    _blocked_users_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemBlocked users"}
    _terms_of_use_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemTerms of Use"}
    _about_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemAbout"}


class Account:
    _sign_out_button = {"by":By.ACCESSIBILITY_ID, "value": "signOutButton"}
    _hide_account_button = {"by":By.ACCESSIBILITY_ID, "value": "accountSettingsHideAccountSwitch"}
    _back_button = {"by": By.ACCESSIBILITY_ID, "value": "accountSettingsHideAccountSwitch"}

class BlockedUsers:
    _edit_button = {"by": By.ACCESSIBILITY_ID, "value": "Edit"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "Cancel"}
    _unblock_selected_button = {"by": By.ACCESSIBILITY_ID, "value": "blockedUsersUnblockSelectedButton"}
    _back_button = {"by": By.ACCESSIBILITY_ID, "value": "backButton"}

class GiftLocators:
    _romatic_gift_category = {"by": By.ACCESSIBILITY_ID, "value": "giftCategoryContainerRomatic"}
    _friendship_gift_category = {"by": By.ACCESSIBILITY_ID, "value": "giftCategoryContainerFriendship"}
    _birthday_gift_category = {"by": By.ACCESSIBILITY_ID, "value": "giftCategoryContainerBirthday"}
    _holidays_gift_category = {"by": By.ACCESSIBILITY_ID, "value": "giftCategoryContainerHolidays"}
    _select_gift_screen_category = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory"}
    _select_gift_screen_credits = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCredits"}
    _category  = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory"}
    _gift_credits = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCredits"}
    _romantic_gift_selector_rose = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/1.png"}
    _romantic_gift_selector_kiss = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/2.png"}
    _romantic_gift_selector_heart = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/3.png"}
    _romantic_gift_selector_bear = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/4.png"}
    _romantic_gift_selector_heart_ring = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/5.png"}
    _romantic_gift_selector_chili = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/6.png"}
    _romantic_gift_selector_pearl = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/7.png"}
    _romantic_gift_selector_heart_rose = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/8.png"}
    _romantic_gift_selector_leaf_rose = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/9.png"}
    _romantic_gift_selector_basket_rose = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/10.png"}
    _romantic_gift_selector_cherry = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/11.png"}
    _romantic_gift_selector_diamond = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/12.png"}
    _friendship_gift_selector_coffee = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/13.png"}
    _friendship_gift_selector_flower = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/14.png"}
    _friendship_gift_selector_strawberry = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/15.png"}
    _friendship_gift_selector_cake = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/16.png"}
    _friendship_gift_selector_butterfly = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/17.png"}
    _friendship_gift_selector_cocktail = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/18.png"}
    _friendship_gift_selector_water_lily = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/19.png"}
    _friendship_gift_selector_balloon = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/20.png"}
    _birthday_gift_selector_cake = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/21.png"}
    _birthday_gift_selector_wishing = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/22.png"}
    _birthday_gift_selector_bear = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/23.png"}
    _birthday_gift_selector_rabbit = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/24.png"}
    _birthday_gift_selector_box = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/25.png"}
    _birthday_gift_selector_balloons = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/26.png"}
    _birthday_gift_selector_rose = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/27.png"}
    _birthday_gift_selector_champain = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/28.png"}
    _holiday_gift_selector_bunny = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/29.png"}
    _holiday_gift_selector_basket_of_eggs = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/30.png"}
    _holiday_gift_selector_egg = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/31.png"}
    _holiday_gift_selector_basket = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/32.png"}
    _holiday_gift_selector_christmas_tree = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/33.png"}
    _holiday_gift_selector_omela = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/34.png"}
    _holiday_gift_selector_hat = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/35.png"}
    _holiday_gift_selector_champain = {"by": By.ACCESSIBILITY_ID, "value": "selectGiftScreenCategory/images/virtual_gifts_new/36.png"}
    _gift_slider_left_arrow = {"by": By.ACCESSIBILITY_ID, "value": "giftSliderLeftArrow"}
    _gift_slider_right_arrow = {"by": By.ACCESSIBILITY_ID, "value": "giftSliderRightArrow"}
    _send_gift_screen_message_input = {"by": By.ACCESSIBILITY_ID, "value": "sendGiftScreenMessageInput"}
    _send_gift_screen_paid_button = {"by": By.ACCESSIBILITY_ID, "value": "sendPaidGiftButton"}

class Chat:
    _all_contacts = {"by": By.ACCESSIBILITY_ID, "value": "allConnections-connectionName}"}
    _chats = {"by": By.ACCESSIBILITY_ID, "value": "chats-connectionName}"}
    visits = {"by": By.ACCESSIBILITY_ID, "value": "visitors-connectionName}"}
    _winks = {"by": By.ACCESSIBILITY_ID, "value": "winks-connectionName}"}
    _favorites = {"by": By.ACCESSIBILITY_ID, "value": "favorites-connectionName}"}
    _birthday = {"by": By.ACCESSIBILITY_ID, "value": "birthdays-connectionName}"}
    _gifts = {"by": By.ACCESSIBILITY_ID, "value": "gifts-connectionName}"}
    _all_contacts_first_contact = {"by": By.XPATH, "value": "(//android.view.ViewGroup[@content-desc=\"chatUser\"])[1]"}
    _back_from_chat = {"by": By.XPATH, "value": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]"}
    _chat_favorite = {"by": By.XPATH, "value": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"}
    _chat_text = {"by": By.XPATH, "value": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText"}
